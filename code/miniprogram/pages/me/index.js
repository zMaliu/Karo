const api = require('../../services/api')

const EMPTY_USER = { nickname: '', phone: '', grade: '', major: '', goal: '' }
const EMPTY_PROFILE = {
  personality: [],
  questionnaire_version: 'v0',
  privacy: { show_online: true, personalized_rec: true, push_enabled: true }
}

Page({
  data: {
    user: EMPTY_USER,
    profile: EMPTY_PROFILE,
    initial: 'K',
    nickname: '',
    editing: false,
    saving: false
  },

  onShow() {
    if (!wx.getStorageSync('token')) {
      wx.reLaunch({ url: '/pages/login/index' })
      return
    }
    this.load()
  },

  load() {
    Promise.all([api.getMe(), api.getProfile()]).then((res) => {
      const user = res[0]
      this.setData({
        user,
        profile: res[1],
        nickname: user.nickname,
        initial: (user.nickname || 'K').slice(0, 1)
      })
    }).catch((err) => this.toast(err))
  },

  startEdit() {
    this.setData({ editing: true })
  },

  onNicknameInput(e) {
    this.setData({ nickname: e.detail.value })
  },

  save() {
    this.setData({ saving: true })
    api.updateMe({ nickname: this.data.nickname }).then((user) => {
      this.setData({
        user,
        editing: false,
        saving: false,
        initial: (user.nickname || 'K').slice(0, 1)
      })
      wx.showToast({ title: '已保存' })
    }).catch((err) => {
      this.setData({ saving: false })
      this.toast(err)
    })
  },

  togglePrivacy(e) {
    const key = e.currentTarget.dataset.key
    const patch = {}
    patch[key] = e.detail.value
    api.updatePrivacy(patch).then((privacy) => {
      this.setData({ 'profile.privacy': privacy })
    }).catch((err) => this.toast(err))
  },

  logout() {
    wx.removeStorageSync('token')
    getApp().globalData.token = ''
    wx.reLaunch({ url: '/pages/login/index' })
  },

  toast(err) {
    wx.showToast({ title: err.message || '操作失败', icon: 'none' })
  }
})
