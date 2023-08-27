import yaml
from sshcheckers import ssh_checkout_negative, upload_files


with open('config.yaml') as f:
    data = yaml.safe_load(f)


def test_step1(make_files):
    # test1
    assert ssh_checkout_negative(data["host"], data["user"], "1111",
    "cd {}; 7z e badarx.7z -o{} -y".format(data['folder_badarx'], data['folder_ext']), "ERROR"), "Test4 Fail"


def test_step2():
    # test2
    assert ssh_checkout_negative(data["host"], data["user"], "1111",
                                 "cd {}; 7z t badarx.7z".format(data['folder_badarx']), "ERROR"), "Test5 Fail"

def test_step3():
    # test3
    assert ssh_checkout_negative(data["host"], data["user"], "1111",
    "cd {}; 7z e -tzip {}/arx1.zp".format(data['folder_in'], data['folder_badarx']), "ERROR"), "Test1 Fail"

def test_step4():
    # test4
    assert ssh_checkout_negative(data["host"], data["user"], "1111",
    "cd {}; 7z a -tzp {}/arx1.zip".format(data['folder_in'], data['folder_badarx']), "ERROR"), "Test1 Fail"

