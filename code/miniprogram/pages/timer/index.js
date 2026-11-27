const api = require('../../services/api')
const { formatClock, formatDuration } = require('../../utils/format')

const MODES = [
  { key: 'pomodoro', label: '番茄' },
  { key: 'focus', label: '自由专注' },
  { key: 'countdown', label: '倒计时' }
]
const SUBJECTS = ['高数', '英语', '编程', '其他']

Page({
  data: {
    modes: MODES,
    subjects: SUBJECTS,
    mode: 'pomodoro',
    subject: '高数',
    status: 'idle',
    clock: '00:00:00',
    todayText: '0 分钟',
    stats: null,
    streak: 0,
    loading: false
  },

  onLoad() {
    if (!wx.getStorageSync('token')) {
      wx.reLaunch({ url: '/pages/login/index' })
      return
    }
    this.syncSession()
    this.loadStats()
  },

  onShow() {
    if (this.data.session) this.startTicker()
  },

  onHide() {
    this.stopTicker()
  },

  onUnload() {
    this.stopTicker()
  },

  syncSession() {
    api.getActiveSession().then((data) => {
      // 重进App时恢复服务端仍在进行的会话
      if (data.session) this.adopt(data.session)
    }).catch((err) => this.toast(err))
  },

  loadStats() {
    api.getStats('today').then((stats) => {
      this.setData({ stats, streak: stats.streak, todayText: formatDuration(stats.today_duration_sec) })
    }).catch((err) => this.toast(err))
  },

  adopt(session) {
    this.baseElapsed = session.elapsed_sec || 0
    this.syncedAt = Date.now()
    this.setData({ session, status: session.status, mode: session.mode, subject: session.subject_tag })
    this.startTicker()
  },

  startTicker() {
    this.stopTicker()
    this.tick()
    this.ticker = setInterval(() => this.tick(), 1000)
  },

  stopTicker() {
    if (this.ticker) {
      clearInterval(this.ticker)
      this.ticker = null
    }
  },

  tick() {
    if (!this.data.session) return
    let elapsed = this.baseElapsed || 0
    if (this.data.status === 'ongoing') {
      elapsed += Math.floor((Date.now() - this.syncedAt) / 1000)
    }
    this.setData({ clock: formatClock(elapsed) })
  },

  onModeTap(e) {
    if (this.data.status !== 'idle') return
    this.setData({ mode: e.currentTarget.dataset.key })
  },

  onSubjectChange(e) {
    this.setData({ subject: this.data.subjects[e.detail.value] })
  },

  start() {
    this.setData({ loading: true })
    api.startSession({ mode: this.data.mode, subject_tag: this.data.subject }).then((session) => {
      this.setData({ loading: false })
      this.adopt(session)
    }).catch((err) => {
      this.setData({ loading: false })
      this.toast(err)
    })
  },

  togglePause() {
    const action = this.data.status === 'paused' ? 'resume' : 'pause'
    api.updateSession(this.data.session.id, action).then((session) => this.adopt(session)).catch((err) => this.toast(err))
  },

  complete() {
    api.completeSession(this.data.session.id).then((data) => {
      this.stopTicker()
      this.setData({ session: null, status: 'idle', clock: '00:00:00', baseElapsed: 0 })
      const streakTip = data.checkin ? '，已连签 ' + data.checkin.streak + ' 天' : ''
      wx.showModal({
        title: '专注完成',
        content: '本次专注 ' + formatDuration(data.session.duration_sec) + streakTip,
        showCancel: false
      })
      this.loadStats()
    }).catch((err) => this.toast(err))
  },

  abort() {
    wx.showModal({
      title: '放弃本次专注？',
      content: '本次时长不计入连签',
      success: (res) => {
        if (!res.confirm) return
        api.abortSession(this.data.session.id).then(() => {
          this.stopTicker()
          this.setData({ session: null, status: 'idle', clock: '00:00:00', baseElapsed: 0 })
          this.loadStats()
        }).catch((err) => this.toast(err))
      }
    })
  },

  toast(err) {
    wx.showToast({ title: err.message || '操作失败', icon: 'none' })
  }
})
