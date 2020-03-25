import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hosts_file(host):
    f = host.file("/etc/hosts")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_sqitch_is_installed(host):
    sqitch_package = host.package("sqitch")
    assert sqitch_package.is_installed


@pytest.mark.parametrize(
    "postgres_packages", ["libdbd-pg-perl", "postgresql-client"])
def test_postgres_packages_are_installed(host, postgres_packages):
    pkg = host.package(postgres_packages)
    assert pkg.is_installed


@pytest.mark.parametrize(
    "sqlite_packages", ["libdbd-sqlite3-perl", "sqlite3"])
def test_sqlite_packages_are_installed(host, sqlite_packages):
    pkg = host.package(sqlite_packages)
    assert pkg.is_installed


@pytest.mark.parametrize(
    "mysql_packages", ["libdbd-mysql-perl", "mysql-client"])
def test_mysql_packages_are_installed(host, mysql_packages):
    pkg = host.package(mysql_packages)
    assert pkg.is_installed
