# Security

Repository này là portfolio sanitized và không nên chứa credential hoặc implementation production.

Nếu phát hiện secret, connection string, dữ liệu người dùng hoặc source production bị commit nhầm, hãy coi đó là sự cố bảo mật: xóa khỏi history, rotate credential liên quan và kiểm tra lại repository PRIVATE/PUBLIC boundary.
