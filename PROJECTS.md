# Project Manifest

Living map of projects in ~/code/. Claude should check this when user mentions something that might be an existing project.

*Last updated: 2026-01-25*

---

## Core Systems

### noos
**Path**: `~/code/noos`
**Purpose**: Universal knowledge graph platform - central DB for all knowledge with per-node privacy
**Status**: ACTIVE
**Stack**: Node.js + Neo4j + React (Docker Compose on single server)
**Features**:
- Per-node privacy (private/public/unlisted/shared)
- External URI annotations (powers Chrome extension)
- Cross-computer file system index
- CLI + API + Claude skill access
- JWT auth + API keys
- Neo4j native labels for node types (:List, :Note, :Issue, etc.)
**Deployment**:
- **Domain**: `https://globalbr.ai`
- **DNS/CDN**: Cloudflare
- **Server**: AWS Lightsail `44.211.180.200`
- **SSH**: `ssh -i ~/.ssh/lightsail-noos.pem ubuntu@44.211.180.200`
- **Neo4j**: `bolt://44.211.180.200:7687`
- **Deploy**: `./deploy.sh`
- **Remote dev**: `USE_REMOTE_DB=true npm run dev`
**Related**: Builds on DenovoEntanglement (Neo4j patterns), RealtimeMeetingOutline (auth)
**Docs**: `ARCHITECTURE.md`, `README.md`

---

## Global Brain Ecosystem

These projects share a common SSO identity (Noos) and work together as an integrated platform.

```
                    ┌─────────────────────────────────────┐
                    │             NOOS                     │
                    │   (Identity + Knowledge Graph)       │
                    │   globalbr.ai                        │
                    └──────────────┬──────────────────────┘
                                   │ SSO
            ┌──────────────────────┼──────────────────────┐
            │                      │                      │
            ▼                      ▼                      ▼
    ┌───────────────┐    ┌─────────────────┐    ┌─────────────────┐
    │ Thoughtstreams│    │    OpenChat     │    │ Thoughtstream   │
    │ (Social Notes)│    │  (Messaging)    │    │ Gemini-Jacob    │
    │ts.globalbr.ai │    │chat.globalbr.ai │    │  (Voice/Capture)│
    └───────────────┘    └─────────────────┘    └─────────────────┘
```

### Shared Infrastructure
- **Database**: All 4 apps share the same Neo4j database (Noos)
- **SSO**: All apps authenticate via Noos (`/auth/authorize` → code exchange)
- **User Graph**: Follows, contacts shared across apps via Noos relationships
- **Notifications**: Global notification service (planned: noos-8bvm)
- **Docker Network**: `noos_default` network connects containers

### Noos Client UI
Noos itself has a React frontend at `~/code/noos/client/` with:
- GraphView, OutlineView, RecentView
- QuickCapture, ListsView, QueryView
- ClaudeSidebar (AI assistant)
This is the 4th UI hitting the same backend.

### Important: Checking Ticket Status
**Always run `bd list --status=open` in the project directory** to get current ticket status.
The "Open Tickets" listed below may be stale. Beads is the source of truth.

### Thoughtstreams
**Path**: `~/code/Thoughtstreams`
**Purpose**: Social network for sharing thoughts - like Twitter but for your knowledge graph
**Status**: ACTIVE
**Stack**: Node.js + Express + Noos storage backend
**Domain**: `https://ts.globalbr.ai`
**Deploy**: `~/code/Thoughtstreams/deploy.sh` → `/opt/thoughtstreams`
**Data**: All posts stored as Noos nodes via `noos-storage.ts`
**Auth**: Noos SSO only (standalone auth removed)
**Open Tickets** (run `bd list --status=open` for current):
- `Thoughtstreams-nt2`: Following/followers with shared social graph
- `Thoughtstreams-na5`: Notification system for replies

### OpenChat
**Path**: `~/code/openchat`
**Purpose**: Real-time messaging app with AI integration
**Status**: ACTIVE
**Stack**: Node.js + WebSockets + Socket.io
**Domain**: `https://chat.globalbr.ai`
**Deploy**: `/opt/openchat`
**Data**: Uses shared Noos Neo4j (same database as all other apps)
**Auth**: Noos SSO (fully integrated - `/api/auth/login` redirects to Noos)
**Open Tickets** (run `bd list --status=open` for current):
- `OpenChat-yg8`: Real-time sidebar + unread indicators

### thoughtstream-gemini-jacob
**Path**: `~/code/thoughtstream-gemini-jacob`
**Purpose**: Voice-first capture app with multi-service posting
**Status**: ACTIVE
**Stack**: Electron + React + Express
**Domain**: `https://notes.globalbr.ai`
**Data**: All notes stored as Noos nodes via `useThoughts.ts` hook (NOT localStorage)
**Auth**: Noos SSO only (standalone auth removed)
**Features**:
- Quick capture with keyboard shortcuts
- Multi-service posting (Twitter, Slack, Telegram, etc.)
- Publish to Thoughtstreams via visibility toggle
- Swift menu bar capture app (`apps/capture/`)
**Open Tickets** (run `bd list --status=open` for current):
- `thoughtstream-gemini-jacob-fhx`: URL routes for individual notes
- `thoughtstream-gemini-jacob-d9c`: Output cells for AI extraction
**Note**: `src/pages/Index.tsx` is LEGACY (uses localStorage) - actual app uses `App.tsx` with Noos

### Cross-Project SSO Epic
All SSO improvements are tracked in Noos epic: `noos-sso-ecosystem`

### noosphere-proto
**Path**: `~/code/noosphere-proto`
**Purpose**: Universal semantic memory layer - unified prototype combining all knowledge projects
**Status**: ⚠️ OBSOLETE (superseded by noos) - planning docs may still be valuable
**Stack**: Python FastAPI + SQLite + D3.js
**Valuable Planning Docs**:
- `ARCHITECTURE.md` - System design thinking
- `USER_STORIES.md` - User journey design
- `USE_CASES.md` - Feature concepts
- `architecture_discussion.md` - Design rationale
**Superseded by**: noos (cloud-native Neo4j version with auth, permissions, CLI)
**Knowledge topics**: Graph schemas, SQLite FTS5, recursive CTE queries, FastAPI, D3 force graphs

### ai-os-apple-data
**Path**: `~/code/ai-os-apple-data`
**Purpose**: Semantic browser foundation - scrapers for Apple data sources
**Status**: Active
**Features**:
- iMessage reader (464K messages)
- Apple Notes reader
- Contacts reader
- Gmail integration
- Partiful/Luma event scraper
- Opportunities detector (Gemini-powered)
- First-contacts correlation
**Vision**: Three-layer architecture (Raw → Structured → Semantic) for unified personal data
**Docs**: `docs/semantic-browser-vision.md`
**Knowledge topics**: Apple SQLite schemas, iMessage parsing, contact lookup (multiple DB sources), Thoughtstream API quirks, Gmail OAuth, Partiful/Luma scraping with stealth mode, phone number normalization

### RealtimeMeetingOutline
**Path**: `~/code/RealtimeMeetingOutline`
**Purpose**: Real-time meeting transcription with entity extraction
**Status**: Active
**Stack**: React + Node.js + Neo4j + AssemblyAI + Claude
**Features**:
- Live transcription
- Entity extraction (People, Orgs, Topics, Decisions, Action Items)
- Neo4j knowledge base with deduplication
- Custom entity lists
**Variants**: `-assemblyai`, `-deepgram` versions exist
**Potential**: Recommended Neo4j backend for ai-os semantic layer
**Knowledge topics**: Neo4j Cypher queries, AssemblyAI streaming, entity deduplication (85% string similarity), WebSocket audio streaming, Claude entity extraction prompts

### mew / mew-mcp
**Path**: `~/code/mew`, `~/code/mew-mcp`
**Purpose**: Production knowledge graph with MCP integration
**Status**: Active
**Features**:
- Graph database
- Claude can query via MCP
**Potential**: Alternative backend for ai-os semantic layer
**Knowledge topics**: MCP server implementation, graph query patterns, Claude tool integration

---

## Personal Memory

### ~/memory
**Path**: `~/memory`
**Purpose**: Personal knowledge management system
**Status**: Active
**Pattern**: Daily notes (Obsidian-style) + cross-posted categories
**Structure**:
- `daily/` - Daily notes (primary view)
- `todos/open.md` - Text-readable todo list
- `insights/` - Lessons learned
- `people/` - Relationship notes
**Integration**: Gets indexed into ai-os for unified queries

---

## Data & Research

### DenovoEntanglement
**Path**: `~/code/DenovoEntanglement`
**Purpose**: Neo4j graph experiments
**Status**: Experimental

### Gemini3Workflowy
**Path**: `~/code/Gemini3Workflowy`
**Purpose**: MarkTree format, brainstorm docs
**Status**: Reference

---

## Apps & Tools

### Clawd (clawdbot)
**Path**: `~/clawd`
**Purpose**: Personal AI assistant (🦊 fox) accessible via Telegram and Slack
**Status**: Active
**Platform**: clawdbot (hosted service)
**Features**:
- Slack integration (API-based, not browser automation)
- Mew knowledge graph queries
- Slack cross-channel search via `~/clawd/canvas/slack-search.sh`
**Docs**:
- `IDENTITY.md` - Agent identity and tool preferences
- `QUICKREF.md` - Command reference
- `TOOLS.md` - Custom tool documentation
- `SLACK_ADMIN.md` - Slack API/permissions guide
**Note**: Different from Claude Code (CLI) - Clawd is a hosted agent for async messaging

### iMessage Companion
**Path**: `~/code/ai-os-apple-data/imessage-companion`
**Purpose**: Floating panel showing context for current Messages.app conversation
**Stack**: Swift macOS app
**Features**: Auto-detects conversation, shows open issues, AI tone suggestions

### FreeNote
**Path**: `~/code/AudNoteSwift/FreeNote`
**Purpose**: Hands-free voice note-taking iOS app with Siri integration
**Status**: Active
**Stack**: Swift, SwiftUI, SwiftData, AVFoundation, App Intents
**Features**:
- "Hey Siri, make a FreeNote" - voice-activated recording
- "Hey Siri, start listening" - continuous listening mode
- Real-time transcription (SFSpeechRecognizer)
- Automatic silence detection (10s timeout)
- Voice commands: "end note", "stop listening"
- Background recording support
**Requirements**: iOS 16+, Xcode 15+
**Beads**: Initialized (prefix: `AudNoteSwift`)

### AltFinder
**Path**: `~/code/AltFinder`
**Purpose**: File browser with semantic potential
**Status**: Active

---

## Web & Publishing

### tmad4000.github.io
**Path**: `~/code/tmad4000.github.io`
**Purpose**: Personal homepage / GitHub Pages
**URL**: https://tmad4000.github.io

### vibe-coding-guide
**Path**: `~/Documents/vibe-coding-guide`
**Purpose**: Guide for AI-assisted coding
**URL**: https://github.com/tmad4000/vibe-coding-guide

---

## Business Projects

### AnswerBot
**Path**: `~/code/AnswerBot`
**Purpose**: Recruitment automation platform
**Stack**: Flask + PostgreSQL + OpenAI
**Status**: Needs work (tracked in beads)

---

## Session References

When a project is discussed in a Claude session, note the session ID here for continuity:

| Project | Session | Date | Notes |
|---------|---------|------|-------|
| ai-os-apple-data | `cef20cac-d64b-4c0b-b2b6-a9de4590d237` | 2025-01-11 | Initial semantic browser vision |
| ~/memory | `cef20cac-d64b-4c0b-b2b6-a9de4590d237` | 2025-01-11 | Created memory system |
| ai-os-apple-data | (continuation) | 2026-01-11 | Experience layer, Slack integration, research capture, AI-as-You bot |
| RealtimeMeetingOutline | (continuation) | 2026-01-11 | Designated as Neo4j backend for ai-os |

---

## How to Use This Manifest

1. **Claude**: Check this file when user mentions something that might be an existing project
2. **Add new projects**: When creating a new project, add an entry here
3. **Update status**: Mark projects as Active/Experimental/Archived
4. **Link sessions**: When having significant discussions about a project, add session ID

---

*This manifest is referenced in ~/.claude/CLAUDE.md*
