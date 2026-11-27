App({
  globalData: {
    baseUrl: 'http://127.0.0.1:5000/api/v1', // 本地联调地址，真机调试改成局域网 IP
    token: ''
  },
  onLaunch() {
    this.globalData.token = wx.getStorageSync('token') || ''
  }
})
