{ pkgs }: {
    deps = [
      pkgs.cowsay
      pkgs.python310Packages.flask
    ];
}