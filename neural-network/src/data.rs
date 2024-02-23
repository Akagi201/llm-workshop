use std::{error::Error, fs::File, io::Read};

use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
pub struct Data {
    pub training_inputs: Vec<[f64; 2]>,
    pub training_outputs: Vec<f64>,
    pub test_inputs: Vec<[f64; 2]>,
}

pub fn get_data() -> Result<Data, Box<dyn Error>> {
    let mut file = File::open("./data.json")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let data: Data = serde_json::from_str(&contents)?;
    Ok(data)
}
