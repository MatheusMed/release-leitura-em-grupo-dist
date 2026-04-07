import json
import subprocess

# python gerar_json.py

# =========================
# 📥 Lê versão atual
# =========================
with open("version.json", "r") as file:
    data = json.load(file)

current_version_code = data.get("versionCode", 0)
current_version_name = data.get("versionName", "0.0.0")

# =========================
# 🔼 Incrementa versão
# =========================
parts = current_version_name.split(".")
parts[-1] = str(int(parts[-1]) + 1)

new_version_name = ".".join(parts)
new_version_code = current_version_code + 1

# =========================
# 🧠 NOVA LÓGICA OTA
# =========================
new_data = {
    "versionCode": new_version_code,
    "previousVersionCode": current_version_code,  # 🔥 ESSENCIAL
    "versionName": new_version_name,
    "apkUrl": f"https://github.com/MatheusMed/release-leitura-em-grupo-dist/releases/download/{new_version_name}/app-debug.apk"
}

# =========================
# 💾 Salva JSON
# =========================
with open("version.json", "w") as file:
    json.dump(new_data, file, indent=2)

print("🚀 Nova versão gerada:")
print("Version Name:", new_version_name)
print("Version Code:", new_version_code)

# =========================
# 🔥 GIT AUTO
# =========================
try:
    subprocess.run(["git", "add", "version.json"], check=True)
    subprocess.run(["git", "commit", "-m", f"update version to {new_version_name}"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("✅ Push realizado com sucesso!")
except subprocess.CalledProcessError:
    print("❌ Erro ao executar git. Verifique configuração.")