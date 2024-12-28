with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "development";
  buildInputs = [
    pkg-config
    python312
    python312Packages.pygame
    pylint
    nixd
  ];
}
