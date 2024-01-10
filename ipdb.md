# ipdb

Today I learnt ...


## ... how to use the Python debugger with the `ipython` niceties


> 2023-01-10T06:39:34+00:00
>
> Set an environment variable in your shell so that using python's `breakpoint()` uses `ipdb` instead of the vanilla `pdb`

#### Recipe

1. Set env var
    ```bash
    echo 'export PYTHONBREAKPOINT="ipdb.set_trace"' >> ~/.zshrc;
    source ~/.zshrc
    ```

2. Add the breakpoint in your test
    ```diff

    def test_mocked_get_access_token():
    +    breakpoint()
        assert True
      
    ```

3. Run it
    ```bash
    pytest -s tests/
    ```

4. `ipdb` paused execution

    ![](img/Screenshot%20from%202024-01-10%2009-44-43.png)