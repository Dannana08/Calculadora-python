# Busca archivos/carpetas relacionados con worldgen, terralith, biome, noise, etc.
# Revisa .zip/.jar (y .rar si tienes rarfile + unrar instalado), mostrando rutas internas.

import os
import zipfile

# ===== CONFIG =====
ROOT = r"C:\Users\PC Gamer\AppData\Roaming\ModrinthApp\profiles\COBBLEVERSE - MODPACK BKN 1.0.0\datapacks"   # <-- CAMBIA ESTO
KEYWORDS = [
    "terralith", "worldgen", "biome", "noise", "overworld",
    "placed_feature", "surface_rule", "multi_noise", "dimension"
]
SCAN_EXTENSIONS = {".zip", ".jar", ".rar"}
# ==================

def matches(name: str) -> bool:
    lower = name.lower()
    return any(k in lower for k in KEYWORDS)

def scan_folder(root_path):
    findings = []

    for current_root, dirs, files in os.walk(root_path):
        # Carpetas
        for d in dirs:
            full_path = os.path.join(current_root, d)
            if matches(d):
                findings.append(("DIR", full_path))

        # Archivos normales
        for f in files:
            full_path = os.path.join(current_root, f)
            ext = os.path.splitext(f)[1].lower()

            if matches(f):
                findings.append(("FILE", full_path))

            # Revisar contenido de zip/jar
            if ext in {".zip", ".jar"}:
                try:
                    with zipfile.ZipFile(full_path, "r") as z:
                        for internal in z.namelist():
                            if matches(internal):
                                findings.append(("ARCHIVE", f"{full_path} -> {internal}"))
                except Exception as e:
                    findings.append(("ERROR", f"{full_path} -> {e}"))

            # Revisar rar (opcional)
            elif ext == ".rar":
                try:
                    import rarfile
                    with rarfile.RarFile(full_path) as rf:
                        for internal in rf.namelist():
                            if matches(internal):
                                findings.append(("ARCHIVE", f"{full_path} -> {internal}"))
                except ImportError:
                    findings.append(("ERROR", f"{full_path} -> rarfile no instalado"))
                except Exception as e:
                    findings.append(("ERROR", f"{full_path} -> {e}"))

    return findings


def main():
    results = scan_folder(ROOT)

    output_file = os.path.join(ROOT, "worldgen_scan_results.txt")

    with open(output_file, "w", encoding="utf-8") as out:
        for kind, path in results:
            line = f"[{kind}] {path}"
            print(line)
            out.write(line + "\n")

    print(f"\nEscaneo completo. Resultado guardado en:\n{output_file}")


if __name__ == "__main__":
    main()