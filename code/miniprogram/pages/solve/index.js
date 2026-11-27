const { PATHS } = require('../../services/api')

// 本页对应模块：solve（AI解题室），契约见 contracts/api.md
// 要接的端点（后端当前 501 骨架，W3 由 C 实现）：
// - POST PATHS.solve.ocr           拍照 OCR 识题（F1）
// - POST PATHS.solve.sessionCreate  提交求解（F2/F3）
// - GET  PATHS.solve.sessionDetail  解题结果（F3）
// - GET  PATHS.solve.wrongList      错题筛选（F5）
// 需要的状态：source(photo/manual)、questionText、subjectTag、result.steps[]、wrongs[]
// TODO(A,W3)：接 mock 解题结果（分步 + 答案 + 知识点标签），结果页给“收入错题本”按钮
Page({
  data: {
    title: 'AI解题室',
    subtitle: '拍照识题 · 分步推导 · 错题本',
    emptyText: '还没有解题记录，拍一道题开始',
    actionText: '拍照解题',
    apiList: [PATHS.solve.ocr, PATHS.solve.sessionCreate, PATHS.solve.wrongList]
  },

  onPrimaryTap() {
    wx.showToast({ title: 'W3 实现：拍照解题', icon: 'none' })
  }
})
