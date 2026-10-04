# Bảo mật và phạm vi công khai

## Repository PRIVATE

Chứa implementation thật: application source, pipeline dữ liệu, Risk Engine, crawler/connector, SQL/schema, tests, workflow và cấu hình deploy.

## Repository PUBLIC

Chỉ chứa nội dung portfolio đã sanitized. Không chứa implementation production hoặc dữ liệu nhạy cảm.

## Dữ liệu

Dự án không chứa vị thế, hạn mức, P&L hoặc dữ liệu nội bộ thật của một ngân hàng. Các danh mục dùng để trình diễn nghiệp vụ là dữ liệu mô phỏng hoặc dữ liệu do người dùng chủ động cung cấp.

## Commercial boundary

Một triển khai thực tế trong tổ chức tài chính cần bổ sung IAM/SSO/RBAC, secret manager, private networking, maker-checker, retention, backup/DR, monitoring và tích hợp với hệ thống nội bộ.
