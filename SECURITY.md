# 🔐 Security Policy

## 📦 Scope

This policy covers the repository's Power BI report, Excel workbook, documentation, and GitHub automation. It does not imply that a hosted Power BI Service environment, gateway, API, or production system exists.

## ✅ Supported version

The latest content on the default branch is the maintained version for this repository. Historical report files may not receive security or data-quality fixes.

## 🚨 Reporting a vulnerability

Please do not publish credentials, private report links, tenant details, or sensitive workbook content in a public issue.

Use GitHub's private vulnerability reporting feature if it is enabled for this repository. Otherwise contact the repository owner through https://github.com/Brajesh31 and provide:

- A concise description of the issue.
- Affected file or workflow.
- Reproduction steps that do not expose secrets or private data.
- Potential impact and suggested mitigation.

## 🛡️ Security expectations

- Keep credentials and tokens out of PBIX, XLSX, screenshots, and commits.
- Review workbook data before making the repository public.
- Use least-privilege GitHub Actions permissions.
- Pin and review third-party workflow actions.
- Avoid printing secrets in workflow logs.
- Keep private Power BI workspace and tenant links out of public documentation.
- Treat downloaded workbooks and PBIX files as untrusted until inspected.
- Verify external links before opening supplied assets.

## 🧯 Response process

1. Acknowledge and assess the report.
2. Reproduce the issue safely.
3. Determine affected files, data, or automation.
4. Prepare a fix or mitigation.
5. Verify the fix and document any remaining risk.
6. Publish a coordinated update when appropriate.

Do not submit confidential incident details through a public discussion.
