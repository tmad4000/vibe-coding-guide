# Project Manifest

Living map of projects in ~/code/. Claude should check this when user mentions something that might be an existing project.

*Last updated: 2026-01-11*

---

## Core Systems

### noosphere-proto
**Path**: `~/code/noosphere-proto`
**Purpose**: Universal semantic memory layer - unified prototype combining all knowledge projects
**Status**: NEW (2026-01-11)
**Stack**: Python FastAPI + SQLite + D3.js
**Features**:
- Unified node/edge/annotation graph model
- 5-mode UI (Personal, Idea Hub, Feedback, Innovation, Meetings)
- Ambient display with voice capture
- Workflowy-style structured view
- Ingestors for Contacts, iMessage, CCI, Otter
- Patch/version system (like git for knowledge)
**Principles**: Frictionless capture, zero-config intelligence, lossless history, invite contribution
**Unifies**: ai-os-apple-data, mew, CCI, collaborative-lists
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

### iMessage Companion
**Path**: `~/code/ai-os-apple-data/imessage-companion`
**Purpose**: Floating panel showing context for current Messages.app conversation
**Stack**: Swift macOS app
**Features**: Auto-detects conversation, shows open issues, AI tone suggestions

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
