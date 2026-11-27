function pad(n) {
  return n < 10 ? '0' + n : '' + n
}

// 秒 -> HH:MM:SS，计时器大数字用
function formatClock(sec) {
  const s = Math.max(0, Math.floor(sec || 0))
  return pad(Math.floor(s / 3600)) + ':' + pad(Math.floor((s % 3600) / 60)) + ':' + pad(s % 60)
}

// 秒 -> 时长文案，统计展示用
function formatDuration(sec) {
  const minutes = Math.floor((sec || 0) / 60)
  if (minutes < 60) return minutes + ' 分钟'
  return Math.floor(minutes / 60) + ' 小时 ' + (minutes % 60) + ' 分钟'
}

module.exports = { formatClock, formatDuration }
