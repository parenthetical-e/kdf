library(rhdf5)
library(tools)


save_kdf <- function(filename, ...){
  # In install say:
  # source("http://bioconductor.org/biocLite.R")
  # biocLite("rhdf5")

  # Look for filename, and delete if it exits
  if(file.exists(filename)){
    file.remove(filename)
  }

  # See if filename ends with
  # {.h5 , .hdf5 , .he5}
  # and add .hdf5 is not
  names <- c('hdf5', 'h5', 'he5')
  if(is.na(pmatch(file_ext(filename), names))){
    filename <- paste(filename, ".hdf5", sep="")
  }

  # Init, and save
  dat <- h5createFile(filename)

  # if length of ... is one assume it's a list
  # otherwise process ... as key-value stream
  if (length(...) == 1) {
    x <- ...
  } else {
    x <- list(...)
  }

  # and save.
  for(k in names(x)){
    h5write(x[k], file=filename, k)
  }

  # Add kdf flag
  h5write(1, file=filename, "kdf")

  # And we're done here.
  H5close()
}


load_kdf <- function(filename){
  # Get the data
  x <- h5read(filename, '/')
  keys <- names(x)

  # Check for a kdf flag, and that it is 1.
  if("kdf" %in% keys){
    if(x[["kdf"]] != 1){
      stop(paste(filename, " is not a kdf file.", sep=""))
    }
  } else {
    stop(paste(filename, " is not a kdf file.", sep=""))
  }

  # Unpack x, producing a key-array list
  # i.e. restructure into a cleaner list
  # from what h5 returns
  loaded <- list()
  for(k in keys){
    if(k == "kdf"){
      next
    }
    loaded[[k]] <- x[[k]][[k]]
  }

  # And we are done here.
  loaded
}
