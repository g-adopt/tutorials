def pytest_sessionstart(session):
    import pyvista
    pyvista.start_xvfb()
