library(readr)
library(dplyr)
library(party)
library(rpart)
library(rpart.plot)
library(ROCR)
set.seed(1200)
titanic3="https://goo.gl/At238b"%>%
  read.csv%>%#read in the data
  select(survived,embarked,sex,sibsp,parch,fare)%>%
  mutate(embarked=factor(embarked),
         sex=factor(sex))
summary(titanic3$fare)
summary(titanic3$sibsp)
summary(titanic3$survived)
.data <- c("training", "test") %>%
  sample(nrow(titanic3), replace = T) %>%
  split(titanic3,.)
rtree_fit <- rpart(survived ~ .,
                   .data$training)
rpart.plot(rtree_fit)
print(rtree_fit)
ctree_fit <- ctree(survived ~ .,
                   data = .data$training)
ctree_roc <- ctree_fit %>%
  predict(newdata = .data$test) %>%
  prediction(.data$test$survived) %>%
  performance("tpr", "fpr")

ROCR::plot(ctree_roc)

rtree_roc <- rtree_fit %>%
  predict(newdata = .data$test) %>%
  prediction(.data$test$survived) %>%
  performance("tpr", "fpr")

ROCR::plot(rtree_roc)


ROCR::plot(ctree_roc,col=70,add=TRUE)




