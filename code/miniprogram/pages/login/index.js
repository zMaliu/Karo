const api = require('../../services/api')

const COUNTDOWN_SEC = 60

Page({
  data: {
    phone: '',
    code: '',
    devCode: '',
    countdown: 0,
    agreed: true,
    loading: false
  },

  onLoad() {
    if (wx.getStorageSync('token')) {
      wx.reLaunch({ url: '/pages/timer/index' })
    }
  },

  onUnload() {
    if (this.timer) clearInterval(this.timer)
  },

  onPhoneInput(e) {
    this.setData({ phone: e.detail.value })
  },

  onCodeInput(e) {
    this.setData({ code: e.detail.value })
  },

  onAgreeChange(e) {
    this.setData({ agreed: e.detail.value.length > 0 })
  },

  sendCode() {
    if (!/^1[3-9]\d{9}$/.test(this.data.phone)) {
      return wx.showToast({ title: '请输入正确的手机号', icon: 'none' })
    }
    if (this.data.countdown > 0) return
    api.sendOtp(this.data.phone).then((data) => {
      // dev 环境后端会把验证码一起返回，正式环境走短信
      this.setData({ devCode: data.dev_code || '', countdown: COUNTDOWN_SEC })
      wx.showToast({ title: '验证码已发送', icon: 'none' })
      this.timer = setInterval(() => {
        const next = this.data.countdown - 1
        this.setData({ countdown: next })
        if (next <= 0) clearInterval(this.timer)
      }, 1000)
    }).catch((err) => {
      wx.showToast({ title: err.message, icon: 'none' })
    })
  },

  login() {
    if (!this.data.agreed) {
      return wx.showToast({ title: '请先勾选用户协议', icon: 'none' })
    }
    if (!this.data.phone || !this.data.code) {
      return wx.showToast({ title: '请填写手机号和验证码', icon: 'none' })
    }
    this.setData({ loading: true })
    api.login(this.data.phone, this.data.code).then((data) => {
      wx.setStorageSync('token', data.access_token)
      getApp().globalData.token = data.access_token
      wx.showToast({ title: data.is_new ? '注册成功' : '欢迎回来', icon: 'none' })
      wx.reLaunch({ url: '/pages/timer/index' })
    }).catch((err) => {
      this.setData({ loading: false })
      wx.showToast({ title: err.message, icon: 'none' })
    })
  }
})
