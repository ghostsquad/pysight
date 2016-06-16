from assertpy import assert_that
import os
from seasalt import assert_that as ss_assert_that, container
from seasalt.exceptions import FileAssertionException
import pytest
from os import path
from tests import RESOURCES_ROOT
from uuid import uuid4

image_tag = 'centos-seasalt'


@pytest.yield_fixture(scope="module")
def container_fixture():
    salt_test1_path = path.join(RESOURCES_ROOT, 'salt_test1')
    with container(image_tag, cwd=salt_test1_path) as c:
        yield c


def test_is_file_given_real_file_expect_no_exception():
    this_file = os.path.abspath(__file__)
    ss_assert_that.file(this_file).is_file()


def test_is_file_given_nonexistent_file_expect_assertion_exception():
    with pytest.raises(FileAssertionException) as e:
        file = str(uuid4())
        ss_assert_that.file(file).is_file()

    assert_that(e).is_not_none()
    assert_that(e.value).contains("not a file")


