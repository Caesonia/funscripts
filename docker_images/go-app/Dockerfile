FROM golang:latest

RUN mkdir /build
WORKDIR /build

RUN export GO111MODULE=on
RUN go get github.com/AdminTurnedDevOps/GoWebAPI/main
RUN cd /build/GoWebAPI/main && git clone https://github.com/AdminTurnedDevOps/GoWebAPI.git

RUN cd /build/GoWebAOI/main && go build

EXPOSE 8080

ENTRYPOINT [ "/build/GoWebAPI/main/main" ]


