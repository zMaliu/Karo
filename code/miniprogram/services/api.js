const { request } = require('./request')

// ===== 全量端点点表（与 contracts/api.md 一一对应，共 53 个）=====
// status: 待实现 = 后端接口已声明、业务待按 功能实现规格书.md 填充（当前统一 501）｜ 后续 = 后续版本
// 页面只从这里取 path，禁止手写 URL
const PATHS = {
  account: {
    otpSend: { method: 'POST', path: '/account/otp/send', status: '待实现' },
    login: { method: 'POST', path: '/account/login', status: '待实现' },
    me: { method: 'GET', path: '/account/me', status: '待实现' },
    meUpdate: { method: 'PATCH', path: '/account/me', status: '待实现' },
    profile: { method: 'GET', path: '/account/profile', status: '待实现' },
    privacy: { method: 'PUT', path: '/account/privacy', status: '待实现' },
    questionnaire: { method: 'POST', path: '/account/questionnaire', status: '后续' },
    devices: { method: 'GET', path: '/account/devices', status: '后续' }
  },
  timer: {
    sessions: { method: 'POST', path: '/timer/sessions', status: '待实现' },
    sessionUpdate: { method: 'PATCH', path: '/timer/sessions/{id}', status: '待实现' },
    complete: { method: 'POST', path: '/timer/sessions/{id}/complete', status: '待实现' },
    abort: { method: 'POST', path: '/timer/sessions/{id}/abort', status: '待实现' },
    active: { method: 'GET', path: '/timer/sessions/active', status: '待实现' },
    list: { method: 'GET', path: '/timer/sessions', status: '待实现' },
    stats: { method: 'GET', path: '/timer/stats', status: '待实现' },
    interrupt: { method: 'POST', path: '/timer/sessions/{id}/interrupt', status: '后续' },
    statsMonth: { method: 'GET', path: '/timer/stats/month', status: '后续' }
  },
  twin: {
    config: { method: 'POST', path: '/twin/config', status: '待实现' },
    profile: { method: 'GET', path: '/twin/profile', status: '待实现' },
    messages: { method: 'GET', path: '/twin/messages', status: '待实现' },
    messageSend: { method: 'POST', path: '/twin/messages', status: '待实现' },
    memorySearch: { method: 'POST', path: '/twin/memory/search', status: '待实现' },
    proactive: { method: 'GET', path: '/twin/proactive', status: '后续' },
    intimacy: { method: 'POST', path: '/twin/intimacy', status: '后续' },
    mood: { method: 'GET', path: '/twin/mood', status: '后续' }
  },
  brain: {
    fileUpload: { method: 'POST', path: '/brain/files', status: '待实现' },
    fileList: { method: 'GET', path: '/brain/files', status: '待实现' },
    fileDetail: { method: 'GET', path: '/brain/files/{id}', status: '后续' },
    noteCreate: { method: 'POST', path: '/brain/notes', status: '待实现' },
    noteDetail: { method: 'GET', path: '/brain/notes/{id}', status: '待实现' },
    noteUpdate: { method: 'PATCH', path: '/brain/notes/{id}', status: '后续' },
    diaryCreate: { method: 'POST', path: '/brain/diaries', status: '后续' },
    diaryList: { method: 'GET', path: '/brain/diaries', status: '后续' },
    chat: { method: 'POST', path: '/brain/chat', status: '待实现' }
  },
  solve: {
    ocr: { method: 'POST', path: '/solve/ocr', status: '待实现' },
    sessionCreate: { method: 'POST', path: '/solve/sessions', status: '待实现' },
    sessionDetail: { method: 'GET', path: '/solve/sessions/{id}', status: '待实现' },
    sessionList: { method: 'GET', path: '/solve/sessions', status: '后续' },
    wrongCreate: { method: 'POST', path: '/solve/wrongs', status: '待实现' },
    wrongList: { method: 'GET', path: '/solve/wrongs', status: '待实现' },
    wrongUpdate: { method: 'PATCH', path: '/solve/wrongs/{id}', status: '后续' },
    wrongDelete: { method: 'DELETE', path: '/solve/wrongs/{id}', status: '后续' },
    hints: { method: 'POST', path: '/solve/hints', status: '后续' },
    variants: { method: 'POST', path: '/solve/variants', status: '后续' }
  },
  palace: {
    room: { method: 'GET', path: '/palace/room', status: '待实现' },
    itemCreate: { method: 'POST', path: '/palace/items', status: '待实现' },
    itemUpdate: { method: 'PATCH', path: '/palace/items/{id}', status: '待实现' },
    itemDelete: { method: 'DELETE', path: '/palace/items/{id}', status: '后续' },
    itemLink: { method: 'POST', path: '/palace/items/{id}/link', status: '待实现' },
    itemReview: { method: 'POST', path: '/palace/items/{id}/review', status: '待实现' },
    itemList: { method: 'GET', path: '/palace/items', status: '后续' },
    rewards: { method: 'GET', path: '/palace/rewards', status: '后续' },
    themeUpdate: { method: 'PATCH', path: '/palace/room', status: '后续' }
  }
}

// 路径参数替换：fill(PATHS.timer.sessionUpdate.path, { id: 12 }) → '/timer/sessions/12'
function fill(path, params) {
  return path.replace(/\{(\w+)\}/g, (match, key) => String(params[key]))
}

module.exports = {
  PATHS,
  fill,
  // ===== 已实现接口封装（页面直接用这些函数，不要手写 URL）=====
  sendOtp(phone) {
    return request(PATHS.account.otpSend.method, PATHS.account.otpSend.path, { phone })
  },
  login(phone, code) {
    return request(PATHS.account.login.method, PATHS.account.login.path, { phone, code })
  },
  getMe() {
    return request(PATHS.account.me.method, PATHS.account.me.path)
  },
  updateMe(patch) {
    return request(PATHS.account.meUpdate.method, PATHS.account.meUpdate.path, patch)
  },
  getProfile() {
    return request(PATHS.account.profile.method, PATHS.account.profile.path)
  },
  updatePrivacy(patch) {
    return request(PATHS.account.privacy.method, PATHS.account.privacy.path, patch)
  },
  startSession(payload) {
    return request(PATHS.timer.sessions.method, PATHS.timer.sessions.path, payload)
  },
  updateSession(id, action) {
    return request(PATHS.timer.sessionUpdate.method, fill(PATHS.timer.sessionUpdate.path, { id }), { action })
  },
  completeSession(id) {
    return request(PATHS.timer.complete.method, fill(PATHS.timer.complete.path, { id }), {})
  },
  abortSession(id) {
    return request(PATHS.timer.abort.method, fill(PATHS.timer.abort.path, { id }), {})
  },
  getActiveSession() {
    return request(PATHS.timer.active.method, PATHS.timer.active.path)
  },
  listSessions() {
    return request(PATHS.timer.list.method, PATHS.timer.list.path)
  },
  getStats(range) {
    return request(PATHS.timer.stats.method, PATHS.timer.stats.path + '?range=' + (range || 'today'))
  }
}
