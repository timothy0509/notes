# AGENTS.md

This repository is an **Obsidian vault** (DSE study notes, synced via Nextcloud, Git-tracked). Its active code project is the **obsidian-opencode** plugin inside `.obsidian/plugins/obsidian-opencode/`.

## Plugin Development

All commands must be run from the plugin directory:

```bash
cd .obsidian/plugins/obsidian-opencode/
bun install
bun run build       # Type-check (tsc -noEmit -skipLibCheck) + esbuild bundle
bun run dev         # esbuild watch mode
bun test            # Run all bun:test tests
bun test tests/ProcessManager.test.ts   # Single test file
```

**Output:** `main.js` (CommonJS, node platform, es2018 target). Obsidian reloads it automatically when the plugin is enabled.

## Verified Architecture

- **Desktop-only.** `manifest.json` declares `isDesktopOnly: true`. The plugin uses `child_process.spawn()` for the server process. Never add mobile-only features.
- **Server URL:** `http://host:port/${btoa(projectDirectory)}`. The plugin verifies readiness by polling `/global/health`.
- **Process lifecycle:** Server starts in `onload()` (if auto-start enabled) and **must** be killed in `onunload()`. `SIGTERM` is sent with a 2s fallback to `SIGKILL`.
- **tsconfig:** ES6 target, ESNext modules, `strictNullChecks`, `noImplicitAny`.
- **esbuild externals:** `obsidian`, `electron`, CodeMirror packages, Node builtins.
- **Default settings:** Port 14096, hostname 127.0.0.1, autoStart false, startupTimeout 15000ms.

## Vault Notes

- The vault uses Obsidian wikilinks (`[[Note Title]]`) and frontmatter YAML.
- Vault subjects are organized via index notes (e.g., `[[BAFS Index]]`).
- The `obsidian-vault` skill is available for vault-specific operations (note creation, linking, searching).

## Plugin Details

See `.obsidian/plugins/obsidian-opencode/AGENTS.md` for naming conventions, Obsidian API patterns, and detailed coding guidelines.
