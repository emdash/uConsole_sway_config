# Initialize
BIN_DIR="${HOME}/bin"
SWAY_LAUNCHER_DESKTOP_VERSION="v1.7.0"
PKGS=()

# Required Pacakges
PKGS+=(sway)
PKGS+=(swaybg)
PKGS+=(swayidle)
PKGS+=(fzf)
PKGS+=(wl-clipboard)
PKGS+=(kbd)
PKGS+=(git)
PKGS+=(x11-utils)
PKGS+=(wev)
PKGS+=(brightnessctl)
PKGS+=(fonts-recommended)
PKGS+=(fonts-noto-color-emoji)
PKGS+=(fonts-symbola)
PKGS+=(ttf-ancient-fonts)
PKGS+=(grim)
PKGS+=(bat)
PKGS+=(delta)

# Recommended packages -- adjust to your preferences.
PKGS+=(emacs-nox)
PKGS+=(neovim)
PKGS+=(netsurf-gtk)
PKGS+=(tmux)
PKGS+=(chafa)
PKGS+=(imv)
PKGS+=(octave)
PKGS+=(maxima)
PKGS+=(wxmaxima)
PKGS+=(bsdgames)
PKGS+=(neofetch)
PKGS+=(firefox-esr)
PKGS+=(blueman)
PKGS+=(pmount)

# sway_launcher_desktop is not available in apt, but it's trivial to
# install from source.
function install_sway_launcher {
    local base="https://raw.githubusercontent.com"
    local user="Biont"
    local repo="sway-launcher-desktop"
    local version="$1"
    local url="${base}/${user}/${repo}/${version}/sway-launcher-desktop.sh"
    curl "${url}" -o "${BIN_DIR}/sway-launcher-desktop.sh"
}

# Setup
mkdir -p "${BIN_DIR}"
install_sway_launcher "${SWAY_LAUNCHER_DESKTOP_VERSION}"
sudo apt install "${PKGS[@]}"
