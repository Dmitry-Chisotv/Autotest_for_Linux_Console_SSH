import subprocess


def ssh_checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if result.returncode == 0 and text in result.stdout:
        return True
    else:
        return False


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if result.returncode != 0 and (text in result.stderr or text in result.stdout):
        return True
    else:
        return False


def checkout_statistics(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    return out
