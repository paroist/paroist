def save_to_file(file_name, jobs):
  file = open(f"{file_name}.csv", "w")
  file.write("Position, Company, Location, Link\n")
  
  for job in jobs:
    file.write(
      f"{job['position']}, {job['company']}, {job['region']}, {job['link']}\n"
      )
  
  file.close()