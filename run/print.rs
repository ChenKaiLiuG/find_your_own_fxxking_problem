use std::fs;
use std::io;

fn main() -> io::Result<()> {
    let filename = "找找自己問題.txt";

    match fs::read_to_string(filename) {
        Ok(contents) => {
            println!("{}", contents);
        }
        Err(e) => {
            eprintln!("無法讀取檔案 '{}': {}", filename, e);
        }
    }

    Ok(())
}
