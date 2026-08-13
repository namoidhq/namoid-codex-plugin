# NamoID Setup Assistant for Codex

[![Validation](https://github.com/namoidhq/namoid-codex-plugin/actions/workflows/validate.yml/badge.svg)](https://github.com/namoidhq/namoid-codex-plugin/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Official Codex marketplace repository for NamoID. The first plugin connects
Codex to NamoID's Setup Assistant MCP and adds a focused workflow for
configuring and diagnosing Customer Identity integrations.

The plugin uses NamoID OAuth in the browser. Permissions remain revocable and
are limited to `setup.read` plus user-approved `setup.write`. The plugin does
not contain credentials or duplicate NamoID configuration logic.

The repository deliberately keeps Codex-specific packaging separate from the
NamoID CLI and Claude Code plugin. All three use the same remote MCP tool and
OAuth permission contracts.

## Security and contributions

The integration is open source under the [MIT License](LICENSE). See [CONTRIBUTING.md](CONTRIBUTING.md)
before proposing changes and [SECURITY.md](SECURITY.md) for private vulnerability
reporting. Never submit NamoID credentials, OAuth tokens, or customer data.

## Links

- [NamoID](https://namoid.in)
- [Documentation](https://docs.namoid.in)
- [Issues](https://github.com/namoidhq/namoid-codex-plugin/issues)
