#R Script to validate CDC's findings.
#Derric Gorothy, Michael Condon, Bryce Melvin  
userFile = readline(prompt = "Please enter the csv file to be used: ")
data = read.csv(file = userFile, header = TRUE)
counter = 0
icd10code = data[,25]
list = NULL
code = readline(prompt= "Please enter a code (in all caps): ")

for(i in icd10code) {
  list = c(list, i)
  if(i == code){
    counter = counter + 1
  }
}
