import yaml
from sshcheckers import ssh_checkout, upload_files
from conftest import save_log

with open('config.yaml') as f:
    data = yaml.safe_load(f)


def test_step0():
    res = []

    upload_files(data["host"], data["user"], "1111","{}/p7zip-full.deb".format(data['local_path']),
                 "{}/p7zip-full.deb".format(data['remote_path']))
    res.append(ssh_checkout(data["host"], data["user"], "1111",
                            "echo '1111' | sudo -S dpkg -i {}/p7zip-full.deb".format(data['remote_path']),"Настраивается пакет"))
    res.append(ssh_checkout(data["host"], data["user"], "1111", "echo '1111' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))

    assert all(res)



def test_step1(make_folders, make_files, start_time):
    # test1 - create the archive
    res1 = ssh_checkout(data["host"], data["user"], "1111", "cd {}; 7z a -t{} {}/arx1.{}".format(data['folder_in'],
                                                             data['type_archive'], data['folder_out'], data['type_archive']
                                                             ), "Everything is Ok"), "Test1 Fail"
    res2 = ssh_checkout(data["host"], data["user"], "1111", "ls {}".format(data['folder_out']), "arx.{}".format(['type_archive'])), "Test1 Fail"
    save_log(start_time, data['start_file'])
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files, start_time):
    # test2
    res = []
    res.append(ssh_checkout(data["host"], data["user"], "1111", "cd {}; 7z a -t{} {}/arx1.{}".format(data['folder_in'],
                                                                 data['type_archive'], data['folder_out'], data['type_archive']
                                                                 ), "Everything is Ok"))
    res.append(ssh_checkout(data["host"], data["user"], "1111", "cd {}; 7z e arx1.{} -o{} -y".format(data['folder_out'], data['type_archive'],
                                                                 data['folder_ext']), "Everything is Ok"))
    for item in make_files:
        res.append(ssh_checkout(data["host"], data["user"], "1111", "ls {}".format(data['folder_ext']), item))
    save_log(start_time, data['start_file'])
    assert all(res)


def test_step3():
    # test3 - check the status
    assert ssh_checkout(data["host"], data["user"], "1111", "cd {}; 7z t {}/arx1.{}".format(data['folder_in'], data['folder_out'],
                                                        data['type_archive']), "Everything is Ok"), "Test1 Fail"


def test_step4():
    # test4 -
    assert ssh_checkout(data["host"], data["user"], "1111", "cd {}; 7z u {}/arx1.{}".format(data['folder_in'], data['folder_out'],
                                                        data['type_archive']), "Everything is Ok"), "Test1 Fail"


def test_step5(clear_folders, make_files, start_time):
    # test5 - create new archive and show consist of the archive
    res = []
    res.append(ssh_checkout(data["host"], data["user"], "1111", "cd {}; 7z a {}/arx1.{}".format(data['folder_in'], data['folder_out'],
                                                            data['type_archive']), "Everything is Ok"))
    for item in make_files:
        res.append(ssh_checkout(data["host"], data["user"], "1111", "cd {}; 7z l arx1.{}".format(data['folder_out'], data['type_archive']), item))
    save_log(start_time, data['start_file'])
    assert all(res)


# def test_step6():



def test_step7():
    assert ssh_checkout(data["host"], data["user"], "1111", "7z d {}/arx1.{}".format(data['folder_out'], data['type_archive']),
                             "Everything is Ok"), "Test1 Fail"
