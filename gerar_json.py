import json
import subprocess

# lê versão atual
with open("version.json", "r") as file:
    data = json.load(file)

# incrementa versão (ex: 0.0.6 → 0.0.7)
parts = data["versionName"].split(".")
parts[-1] = str(int(parts[-1]) + 1)

new_version = ".".join(parts)
new_code = data["versionCode"] + 1

# cria novo JSON
new_data = {
    "versionCode": new_code,
    "versionName": new_version,
    "apkUrl": f"https://github.com/MatheusMed/release-leitura-em-grupo-dist/releases/download/{new_version}/app-debug.apk"
}

# salva arquivo
with open("version.json", "w") as file:
    json.dump(new_data, file, indent=2)

print("Nova versão:", new_version)

# 🔥 comandos git
try:
    subprocess.run(["git", "add", "version.json"], check=True)
    subprocess.run(["git", "commit", "-m", f"update version to {new_version}"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("🚀 Push realizado com sucesso!")
except subprocess.CalledProcessError:
    print("❌ Erro ao executar git. Verifique configuração.")