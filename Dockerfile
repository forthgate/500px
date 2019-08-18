FROM python:2.7-slim-stretch as builder
MAINTAINER forthgate@gmail.com
ENV DEBIAN_FRONTEND noninteractive
RUN mkdir -p /usr/share/man/man1mkdir -p /usr/share/man/man1
RUN apt-get update && apt-get install -y\
    software-properties-common ninja-build git lsb-release\
    sudo curl wget g++-arm-linux-gnueabihf openjdk-8-jdk\
    ca-certificates-java ant ant-optional ttf-dejavu libnss3
RUN git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git /opt/depot_tools
ENV PATH="/opt/depot_tools:${PATH}"
RUN mkdir /opt/depot_tools/chromium && cd /opt/depot_tools/chromium && fetch --no-history chromium
WORKDIR /opt/depot_tools/chromium/src/
RUN ./build/install-build-deps.sh --no-prompt && mkdir -p out/Headless
RUN echo 'import("//build/args/headless.gn")' > out/Headless/args.gn && echo 'is_debug = false' >> out/Headless/args.gn
RUN gn gen out/Headless
RUN ninja -C out/Headless headless_shell

FROM python:3.5.7-slim-buster
WORKDIR /opt
COPY . ./
COPY --from=builder /opt/depot_tools/chromium/src/out/Headless/ ./webdriver/
RUN chmod +x ./webdriver/chromedriver
RUN pip3 install -r requirements.txt
CMD ["python", "500.py"]
