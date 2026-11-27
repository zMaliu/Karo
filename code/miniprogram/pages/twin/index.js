const { PATHS } = require('../../services/api')

// 本页对应模块：twin（数字孪生 / 学伴），契约见 contracts/api.md
// 要接的端点（后端接口已声明、业务待实现，按 功能实现规格书 填充后替换 mock）：
// - POST PATHS.twin.config       形象选择（F2）
// - GET  PATHS.twin.profile      亲密度/学伴资料（F7）
// - GET  PATHS.twin.messages     历史会话（F8）
// - POST PATHS.twin.messageSend  流式对话（F3）
// 需要的状态：avatarId、messages[]、streaming（流式气泡）、intimacy
// TODO(A,W3)：接 mock 流式对话（request 暂不支持 chunked，先整段返回）
Page({
  data: {
    title: '学伴',
    subtitle: '数字孪生 · 懂你目标的专属学习搭子',
    emptyText: '还没有学伴，先选一个形象',
    actionText: '选择形象',
    apiList: [PATHS.twin.config, PATHS.twin.profile, PATHS.twin.messageSend]
  },

  onPrimaryTap() {
    wx.showToast({ title: 'W3 实现：形象选择', icon: 'none' })
  }
})
