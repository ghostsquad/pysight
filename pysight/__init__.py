from seasalt.assert_that.assertion_builders.FileAssertionBuilder import FileAssertionBuilder
from seasalt.assert_that.assertion_builders.GroupAssertionBuilder import GroupAssertionBuilder
from seasalt.assert_that.assertion_builders.PackageAssertionBuilder import PackageAssertionBuilder
from seasalt.assert_that.assertion_builders.ProcessAssertionBuilder import ProcessAssertionBuilder
from seasalt.assert_that.assertion_builders.UserAssertionBuilder import UserAssertionBuilder
from seasalt.assert_that.assertion_builders.CommandAssertionBuilder import CommandAssertionBuilder


def command(val, description=''):
    return CommandAssertionBuilder(val, description)


def file(val, description=''):
    return FileAssertionBuilder(val, description)


def user(val, description=''):
    return UserAssertionBuilder(val, description)


def group(val, description=''):
    return GroupAssertionBuilder(val, description)


def package(val, description=''):
    return PackageAssertionBuilder(val, description)


def process(val, description=''):
    return ProcessAssertionBuilder(val, description)

