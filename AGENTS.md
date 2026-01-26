# AGENTS.md - Development Guidelines

This document provides essential information for AI coding agents working on this repository, which primarily contains an Obsidian vault and the **obsidian-opencode** plugin.

## 1. Project Overview
- **Vault:** An Obsidian knowledge base.
- **Plugin:** `obsidian-opencode` (located in `.obsidian/plugins/obsidian-opencode/`).
- **Core Functionality:** Embeds the OpenCode AI assistant via an iframe, manages a local server process, and provides a sidebar view.
- **Tech Stack:** TypeScript, Obsidian Plugin API, Bun, esbuild, Node.js (child_process).

## 2. Environment & Commands
Commands should be run from the plugin directory: `cd .obsidian/plugins/obsidian-opencode/`.

| Task | Command |
|------|---------|
| Install Deps | `bun install` |
| Build (Prod) | `bun run build` |
| Dev (Watch) | `bun run dev` |
| Run All Tests | `bun test` |
| Run Single Test| `bun test tests/ProcessManager.test.ts` |
| Type Check | `bun run tsc -noEmit` |

## 3. Code Style & Conventions

### Naming Conventions
- **Classes / Types / Interfaces:** `PascalCase` (e.g., `OpenCodePlugin`, `ProcessState`).
- **Variables / Functions:** `camelCase` (e.g., `startServer`, `projectDirectory`).
- **Constants:** `UPPER_CASE` or `camelCase` (e.g., `DEFAULT_SETTINGS`, `OPENCODE_ICON_NAME`).
- **Private Members:** `camelCase` without underscores (e.g., `private processManager`).
- **Files:** `PascalCase` for classes, `camelCase` or `lowercase` for entries (e.g., `ProcessManager.ts`, `main.ts`).

### TypeScript Patterns
- **Strict Typing:** `strictNullChecks` is enabled. Always handle `null` and `undefined`.
- **Explicit Returns:** Provide explicit return types for all public methods and complex functions.
- **Async/Await:** Prefer `async/await` over raw `Promise` chains.
- **State Enums:** Use union types for state management (e.g., `"stopped" | "starting" | "running" | "error"`).

### Imports & Exports
- Group imports:
  1. Obsidian modules (`obsidian`)
  2. Built-in Node modules (`child_process`, `path`)
  3. Internal modules
- Use `import type` for type-only imports where possible.
- Default export the main `Plugin` class in `main.ts`.

### Obsidian API Usage
- **Lifecycle:** Use `onload()` and `onunload()` for setup and cleanup.
- **DOM:** Use Obsidian's helper methods: `createEl()`, `createDiv()`, `setIcon()`. Avoid `innerHTML` for security.
- **Commands:** Register commands in `onload()` using `this.addCommand()`.
- **Settings:** Use `PluginSettingTab` and `saveData()` / `loadData()`.

### Error Handling
- Use `Notice` from the Obsidian API to show non-blocking errors to the user.
- In `ProcessManager`, use the `setError` pattern to update internal state and log to console.
- Always include `try/catch` blocks around network calls (e.g., `fetch`) and process operations.

## 4. Testing Guidelines
- **Framework:** `bun:test`.
- **Location:** All tests reside in the `tests/` directory.
- **Patterns:**
  - Use `describe` blocks to group functionality.
  - Use `beforeAll` for environment checks (e.g., verifying binary existence).
  - Use `afterEach` for cleanup (e.g., killing child processes).
  - Mock Obsidian API if needed, or focus tests on logic-heavy classes like `ProcessManager`.

```typescript
// Example test structure
import { describe, test, expect, afterEach } from "bun:test";

describe("Logic Component", () => {
  afterEach(() => { /* cleanup */ });
  test("should perform expected action", async () => {
    // ...
  });
});
```

## 5. Process Management (Specific to Plugin)
- The plugin spawns a local server using `child_process.spawn`.
- **Lifecycle:** The server should be started in `onload` (if auto-start is enabled) and MUST be killed in `onunload`.
- **Health Checks:** Implement polling with a timeout to verify the server is ready before transitioning to the `running` state.
- **Port Management:** Allow user-configurable ports via settings.

## 6. CSS & Styling
- Styles should be placed in `styles.css` if global, or applied via `cls` in `createEl`.
- Follow Obsidian's CSS variable conventions (e.g., `--text-normal`, `--interactive-accent`) for theme compatibility.

## 7. File Structure
```text
.obsidian/plugins/obsidian-opencode/
├── src/
│   ├── main.ts           # Entry point
│   ├── ProcessManager.ts # Child process handling
│   ├── OpenCodeView.ts   # Sidebar UI (Iframe)
│   ├── SettingsTab.ts    # Plugin settings
│   ├── icons.ts          # Custom SVG icons
│   └── types.ts          # Shared types & defaults
├── tests/                # Bun tests
├── esbuild.config.mjs    # Build script
├── package.json          # Dependencies & scripts
└── manifest.json         # Obsidian plugin manifest
```

## 8. Development Workflow
1. Run `bun run dev` to start esbuild in watch mode.
2. Changes to `main.js` will be detected by Obsidian (if the plugin is enabled).
3. Always run `bun test` before committing changes to ensure process logic remains stable.
4. Ensure `bun run build` succeeds (it includes type checking).

## 9. Rule Files
*(No .cursorrules or .github/copilot-instructions.md found in this repository)*
*(If rules are added, they should be incorporated here)*
