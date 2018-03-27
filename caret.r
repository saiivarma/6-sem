library(caret)
library(rpart.plot)
data_url <- c(<URL>)
download.file(url = data_url, destfile = "car.data")
car_df <- read.csv("car.data", sep=',', header = FALSE)
set.seed(3033)
intrain <- createDataPartition(y = car_df$V7, p = 0.7, list = FALSE)
training <- car_df[intrain,]
testing <- car_df[-intrain,]
trctrl <- trainControl(method = "repeatedcv", number = 10, repeats = 3)
set.seed(3333)
dtree_fit <- train(V7~., data = training, method = "rpart", parms = list(split = "information"), trControl = trctrl, tuneLength = 10)
prp(dtree_fit$finalModel, box.palette = "Reds", tweak = 1.2)