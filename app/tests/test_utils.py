import os
from utils import get_env_var

def test_get_env_var_fail():
    try:
        get_env_var('not-existing-env')
        assert False, 'Expected KeyError exception was skipped'
    except Exception:
        assert True, 'Expected KeyError exception was raised'


def test_get_env_var_success():
    os.environ['MY_ENV_VAR'] = 'my-env-var'
    try:
        env_var = get_env_var('MY_ENV_VAR')
        assert env_var == 'my-env-var'
        assert not env_var == 'wrong-var'
    except Exception:
        assert False
