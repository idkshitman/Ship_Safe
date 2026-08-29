<p align="center">
  <a href="https://github.com/idkshitman/Ship_Safe"><img src="https://img.shields.io/badge/Ship_Safe-PR%20Test%20Runner-black?style=for-the-badge" alt="ShipSafe"/></a>
  <a href="https://trueforge.dev"><img src="https://img.shields.io/badge/TrueForge-0.2.0--rc.0-7C3AED?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2Zz4=" alt="TrueForge"/></a>
  <a href="https://www.wemakedevs.org/hackathons/trueforge"><img src="https://img.shields.io/badge/Hackathon-File%20TF--007-FFB800?style=for-the-badge" alt="TF-007"/></a>
  <a href="https://github.com/idkshitman/Ship_Safe/pull/3"><img src="https://img.shields.io/badge/Qodo-Reviewed-00D9FF?style=for-the-badge" alt="Qodo"/></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-A3FF12?style=for-the-badge" alt="MIT"/></a>
</p>

<h1 align="center">ShipSafe — PR Test Runner on TrueForge</h1>
<p align="center"><b>Give it a PR URL → it fetches diff, fans out to 3 subagents, runs <code>npm test</code> in a Daytona sandbox, and pauses for human <code>Allow</code> before posting.</b><br/>Live demo on <a href="https://github.com/idkshitman/Ship_Safe/pull/3">PR #3</a> • 14 tool calls • Sandbox FAIL → Comment posted</p>

<p align="center">
  <a href="https://youtu.be/yE7xYjJ88fI">
    <img src="https://img.shields.io/badge/Demo-Video%20(3min)-FF0000?style=for-the-badge&logo=youtube" alt="Demo"/>
  </a>
  <a href="https://github.com/idkshitman/Ship_Safe/pull/3">
    <img src="https://img.shields.io/badge/Qodo-Reviewed-00D9FF?style=for-the-badge" alt="Qodo"/>
  </a>
</p>

---

## ✨ Demo

> <img width="2558" height="1368" alt="image" src="https://github.com/user-attachments/assets/aa9dcb8a-8540-473c-941f-a043fbf201eb" />


| Step | What you see | Screenshot |
|------|--------------|------------|
| **1. Fetch** | `pull_request_read` — 3 files + diff | `Agent steps: 14 tool calls` |
| **2. Subagents** | 3 parallel per file | `src/app.js: BLOCKER` · `test.js: LOW` · `package.json: LOW` |
| **3. Sandbox** | Daytona — `npm test` → `FAIL: add(2,3)=-1` | `Validate in Python` fallback (proves sandbox-as-tool) |
| **4. Pause** | `Tool Approval Required for add_issue_comment` | `Allow / Deny` buttons |
| **5. Post** | `Comment posted successfully` → [[PR #3 comment](https://github.com/idkshitman/Ship_Safe/pull/3#issuecomment-5462257328)] | ID `5461998710` |

**Session:** Refresh browser mid-run → history persists.

---

## 🧩 How It Uses TrueForge (Harness Proof)

| Harness | How ShipSafe uses it |
|---------|----------------------|
| **🔌 Tool** | GitHub MCP `pull_request_read`, `get_file_contents` — 14 calls |
| **🧊 Sandbox** | Daytona `sandbox as tool` — runs `npm test` / `python test.py` isolated |
| **✋ Approval** | 2 gates — agent `Approve and post?` + harness `add_issue_comment` → `Allow` |
| **🤖 Subagents** | 3 parallel reviews per file — keeps root context clean |
| **🔄 Session** | Survives refresh/reconnect via Postgres + Redis |
| **🤖 Model** | `openrouter/z-ai-glm-5-2-free` via Custom provider |

---

## 🏗️ Architecture

```mermaid
graph LR
    A[/review PR URL/] --> B[Parse owner/repo/PR]
    B --> C[GitHub MCP<br/>pull_request_read]
    C --> D[Subagents x3<br/>per file]
    C --> E[Sandbox<br/>npm test / python]
    D --> F[Merge + Summarize]
    E --> F
    F --> G{Pause for human<br/>Allow/Deny}
    G -->|Allow| H[add_issue_comment<br/>PR #]
    G -->|Deny| I[Exit]
