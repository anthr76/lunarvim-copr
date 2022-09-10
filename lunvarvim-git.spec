%global debug_package %{nil}
%global forgeurl    https://github.com/LunarVim/LunarVim
%global commit      2519e07423e2f6ce4cbed6483305dcaa5bbabf4e
%global date        20220909
%global realname    lunarvim

%global pkgrel  1


Name:           %{realname}-git
Version:        1.1.4~%{date}g%(c=%{commit}; echo ${c:0:7}) 
%forgemeta -a
%undefine  distprefix0
Release:        0.%{pkgrel}%{?dist}
Summary:        An IDE layer for Neovim with sane defaults. Completely free and community driven.

License:        GPLv3
URL:            https://www.lunarvim.org
Source0:        %{forgesource0}

BuildRequires: desktop-file-utils

Requires:   neovim
Requires:   tree-sitter-cli
Requires:   python3-neovim
Requires:   fd-find
Requires:   ripgrep

%description
LunarVim is an opinionated, extensible, and fast IDE layer for Neovim


%prep
%setup -q -n %{extractdir0}
cat <<EOF >lvim
#!/bin/sh
export LUNARVIM_RUNTIME_DIR="%{_datadir}/%{realname}"
export LUNARVIM_CONFIG_DIR="%{_sysconfdir}/lvim"
export LUNARVIM_CACHE_DIR="%{_localstatedir}/cache/%{realname}"
exec %{_bindir}/nvim -u "\$LUNARVIM_RUNTIME_DIR/lvim/init.lua" "\$@"
EOF

%build

%install
desktop-file-validate utils/desktop/lvim.desktop
desktop-file-install utils/desktop/lvim.desktop
mkdir -p  %{buildroot}/%{_localstatedir}/cache/%{realname}
install -D -p -m 0644 utils/installer/config.example.lua %{buildroot}/%{_sysconfdir}/lvim/config.lua
install -D -p -m 0755 lvim %{buildroot}%{_bindir}/lvim

install -D -p -m 0644 init.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim
install -D -p -m 0644 ftdetect/json.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/ftdetect/json.lua
install -D -p -m 0644 ftdetect/plaintex.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/ftdetect/plaintex.lua
install -D -p -m 0644 ftdetect/zig.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/ftdetect/zig.lua
install -D -p -m 0644 lua/lvim/bootstrap.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/bootstrap.lua
install -D -p -m 0644 lua/lvim/config/defaults.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/config/defaults.lua
install -D -p -m 0644 lua/lvim/config/init.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/config/init.lua
install -D -p -m 0644 lua/lvim/config/settings.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/config/settings.lua
install -D -p -m 0644 lua/lvim/core/alpha.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/alpha.lua
install -D -p -m 0644 lua/lvim/core/alpha/dashboard.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/alpha/dashboard.lua
install -D -p -m 0644 lua/lvim/core/alpha/startify.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/alpha/startify.lua
install -D -p -m 0644 lua/lvim/core/autocmds.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/autocmds.lua
install -D -p -m 0644 lua/lvim/core/autopairs.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/autopairs.lua
install -D -p -m 0644 lua/lvim/core/bufferline.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/bufferline.lua
install -D -p -m 0644 lua/lvim/core/builtins/init.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/builtins/init.lua
install -D -p -m 0644 lua/lvim/core/cmp.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/cmp.lua
install -D -p -m 0644 lua/lvim/core/commands.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/commands.lua
install -D -p -m 0644 lua/lvim/core/comment.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/comment.lua
install -D -p -m 0644 lua/lvim/core/dap.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/dap.lua
install -D -p -m 0644 lua/lvim/core/gitsigns.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/gitsigns.lua
install -D -p -m 0644 lua/lvim/core/info.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/info.lua
install -D -p -m 0644 lua/lvim/core/log.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/log.lua
install -D -p -m 0644 lua/lvim/core/lualine/colors.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/lualine/colors.lua
install -D -p -m 0644 lua/lvim/core/lualine/components.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/lualine/components.lua
install -D -p -m 0644 lua/lvim/core/lualine/conditions.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/lualine/conditions.lua
install -D -p -m 0644 lua/lvim/core/lualine/init.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/lualine/init.lua
install -D -p -m 0644 lua/lvim/core/lualine/styles.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/lualine/styles.lua
install -D -p -m 0644 lua/lvim/core/lualine/utils.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/lualine/utils.lua
install -D -p -m 0644 lua/lvim/core/mason.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/mason.lua
install -D -p -m 0644 lua/lvim/core/notify.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/notify.lua
install -D -p -m 0644 lua/lvim/core/nvimtree.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/nvimtree.lua
install -D -p -m 0644 lua/lvim/core/project.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/project.lua
install -D -p -m 0644 lua/lvim/core/telescope.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/telescope.lua
install -D -p -m 0644 lua/lvim/core/telescope/custom-finders.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/telescope/custom-finders.lua
install -D -p -m 0644 lua/lvim/core/terminal.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/terminal.lua
install -D -p -m 0644 lua/lvim/core/treesitter.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/treesitter.lua
install -D -p -m 0644 lua/lvim/core/which-key.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/core/which-key.lua
install -D -p -m 0644 lua/lvim/impatient.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/impatient.lua
install -D -p -m 0644 lua/lvim/impatient/profile.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/impatient/profile.lua
install -D -p -m 0644 lua/lvim/interface/popup.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/interface/popup.lua
install -D -p -m 0644 lua/lvim/interface/text.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/interface/text.lua
install -D -p -m 0644 lua/lvim/keymappings.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/keymappings.lua
install -D -p -m 0644 lua/lvim/lsp/config.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/config.lua
install -D -p -m 0644 lua/lvim/lsp/handlers.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/handlers.lua
install -D -p -m 0644 lua/lvim/lsp/init.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/init.lua
install -D -p -m 0644 lua/lvim/lsp/manager.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/manager.lua
install -D -p -m 0644 lua/lvim/lsp/null-ls/code_actions.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/null-ls/code_actions.lua
install -D -p -m 0644 lua/lvim/lsp/null-ls/formatters.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/null-ls/formatters.lua
install -D -p -m 0644 lua/lvim/lsp/null-ls/init.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/null-ls/init.lua
install -D -p -m 0644 lua/lvim/lsp/null-ls/linters.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/null-ls/linters.lua
install -D -p -m 0644 lua/lvim/lsp/null-ls/services.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/null-ls/services.lua
install -D -p -m 0644 lua/lvim/lsp/peek.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/peek.lua
install -D -p -m 0644 lua/lvim/lsp/providers/jsonls.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/providers/jsonls.lua
install -D -p -m 0644 lua/lvim/lsp/providers/sumneko_lua.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/providers/sumneko_lua.lua
install -D -p -m 0644 lua/lvim/lsp/providers/tailwindcss.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/providers/tailwindcss.lua
install -D -p -m 0644 lua/lvim/lsp/providers/vuels.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/providers/vuels.lua
install -D -p -m 0644 lua/lvim/lsp/providers/yamlls.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/providers/yamlls.lua
install -D -p -m 0644 lua/lvim/lsp/templates.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/templates.lua
install -D -p -m 0644 lua/lvim/lsp/utils.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/lsp/utils.lua
install -D -p -m 0644 lua/lvim/plugin-loader.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/plugin-loader.lua
install -D -p -m 0644 lua/lvim/plugins.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/plugins.lua
install -D -p -m 0644 lua/lvim/utils.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/utils.lua
install -D -p -m 0644 lua/lvim/utils/functions.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/utils/functions.lua
install -D -p -m 0644 lua/lvim/utils/git.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/utils/git.lua
install -D -p -m 0644 lua/lvim/utils/hooks.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/utils/hooks.lua
install -D -p -m 0644 lua/lvim/utils/table.lua -t %{buildroot}/%{_datadir}/%{realname}/lvim/lua/lvim/utils/table.lua

%check


%files
%license LICENSE
%doc README.md
%{_bindir}/lvim
%dir %{_sysconfdir}/lvim
%{_sysconfdir}/lvim/config.lua
%{_datadir}/applications/lvim.desktop
%{_datadir}/%{realname}/lvim/init.lua
%dir %{_datadir}/%{realname}/lvim/ftdetect
%{_datadir}/%{realname}/lvim/ftdetect/json.lua
%{_datadir}/%{realname}/lvim/ftdetect/plaintex.lua
%{_datadir}/%{realname}/lvim/ftdetect/zig.lua
%dir %{_datadir}/%{realname}/lvim/lua/lvim
%{_datadir}/%{realname}/lvim/lua/lvim/bootstrap.lua/bootstrap.lua
%{_datadir}/%{realname}/lvim/lua/lvim/config/defaults.lua/defaults.lua
%{_datadir}/%{realname}/lvim/lua/lvim/config/init.lua/init.lua
%{_datadir}/%{realname}/lvim/lua/lvim/config/settings.lua/settings.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/alpha.lua/alpha.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/alpha/dashboard.lua/dashboard.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/alpha/startify.lua/startify.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/autocmds.lua/autocmds.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/autopairs.lua/autopairs.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/bufferline.lua/bufferline.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/builtins/init.lua/init.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/cmp.lua/cmp.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/commands.lua/commands.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/comment.lua/comment.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/dap.lua/dap.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/gitsigns.lua/gitsigns.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/info.lua/info.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/log.lua/log.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/lualine/colors.lua/colors.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/lualine/components.lua/components.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/lualine/conditions.lua/conditions.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/lualine/init.lua/init.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/lualine/styles.lua/styles.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/lualine/utils.lua/utils.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/mason.lua/mason.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/notify.lua/notify.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/nvimtree.lua/nvimtree.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/project.lua/project.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/telescope.lua/telescope.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/telescope/custom-finders.lua/custom-finders.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/terminal.lua/terminal.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/treesitter.lua/treesitter.lua
%{_datadir}/%{realname}/lvim/lua/lvim/core/which-key.lua/which-key.lua
%{_datadir}/%{realname}/lvim/lua/lvim/impatient.lua/impatient.lua
%{_datadir}/%{realname}/lvim/lua/lvim/impatient/profile.lua/profile.lua
%{_datadir}/%{realname}/lvim/lua/lvim/interface/popup.lua/popup.lua
%{_datadir}/%{realname}/lvim/lua/lvim/interface/text.lua/text.lua
%{_datadir}/%{realname}/lvim/lua/lvim/keymappings.lua/keymappings.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/config.lua/config.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/handlers.lua/handlers.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/init.lua/init.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/manager.lua/manager.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/null-ls/code_actions.lua/code_actions.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/null-ls/formatters.lua/formatters.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/null-ls/init.lua/init.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/null-ls/linters.lua/linters.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/null-ls/services.lua/services.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/peek.lua/peek.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/providers/jsonls.lua/jsonls.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/providers/sumneko_lua.lua/sumneko_lua.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/providers/tailwindcss.lua/tailwindcss.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/providers/vuels.lua/vuels.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/providers/yamlls.lua/yamlls.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/templates.lua/templates.lua
%{_datadir}/%{realname}/lvim/lua/lvim/lsp/utils.lua/utils.lua
%{_datadir}/%{realname}/lvim/lua/lvim/plugin-loader.lua/plugin-loader.lua
%{_datadir}/%{realname}/lvim/lua/lvim/plugins.lua/plugins.lua
%{_datadir}/%{realname}/lvim/lua/lvim/utils.lua/utils.lua
%{_datadir}/%{realname}/lvim/lua/lvim/utils/functions.lua/functions.lua
%{_datadir}/%{realname}/lvim/lua/lvim/utils/git.lua/git.lua
%{_datadir}/%{realname}/lvim/lua/lvim/utils/hooks.lua/hooks.lua
%{_datadir}/%{realname}/lvim/lua/lvim/utils/table.lua/table.lua


%changelog
%autochangelog
