{
  inputs.nixpkgs.url = "nixpkgs/nixos-23.11";

  outputs =
    { self
    , nixpkgs
    }:
    let
      pkgs = import nixpkgs { system = "x86_64-linux"; };
    in
    {
      devShells.x86_64-linux.rofi-rust = pkgs.mkShell {
        name = "assaracus";
        buildInputs = [
          pkgs.vscode-langservers-extracted
          pkgs.nodePackages.prettier
        ];
      };
    };
}
