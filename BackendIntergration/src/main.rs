use pyo3::prelude::*;

fn main() -> PyResult<()> {

    let py_code = include_str!("test.py");
    Python::with_gil(|py| {
        let test = PyModule::from_code(py, py_code, "test", "test")?;
        let res: String = test.getattr("somestuff")?.call0()?.extract()?;
        dbg!(res);
        // let sys = py.import("sys")?;
        // let version: String = sys.getattr("version")?.extract()?;

        // let locals = [("os", py.import("os")?)].into_py_dict(py);
        // let code = "os.getenv('USER') or os.getenv('USERNAME') or 'Unknown'";
        // let user: String = py.eval(code, None, Some(&locals))?.extract()?;

        // println!("Hello {}, I'm Python {}", user, version);
        Ok(())
    })
}