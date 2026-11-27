const TIMEOUT = 10000

function clientTimezone() {
  try {
    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone
    if (tz) return tz
  } catch (e) {
    // 部分基础库没有 Intl，回退到系统信息
  }
  try {
    return wx.getSystemInfoSync().timezone || 'Asia/Shanghai'
  } catch (e) {
    return 'Asia/Shanghai'
  }
}

function toLogin() {
  wx.removeStorageSync('token')
  wx.reLaunch({ url: '/pages/login/index' })
}

// 统一解包 { data, meta } 信封；401 清登录态并回登录页
function request(method, path, data) {
  const token = wx.getStorageSync('token') || ''
  return new Promise((resolve, reject) => {
    wx.request({
      url: getApp().globalData.baseUrl + path,
      method,
      data: data || {},
      timeout: TIMEOUT,
      header: {
        'Content-Type': 'application/json',
        'X-Client-Timezone': clientTimezone(),
        Authorization: token ? 'Bearer ' + token : ''
      },
      success(res) {
        const body = res.data || {}
        if (res.statusCode === 401) {
          toLogin()
          return reject({ code: 'UNAUTHORIZED', message: '登录已过期，请重新登录' })
        }
        if (res.statusCode >= 200 && res.statusCode < 300) {
          return resolve(body.data)
        }
        const err = body.error || {}
        reject({ code: err.code || 'HTTP_' + res.statusCode, message: err.message || '请求失败' })
      },
      fail() {
        reject({ code: 'NETWORK_ERROR', message: '网络异常，请确认后端已启动' })
      }
    })
  })
}

module.exports = { request }
