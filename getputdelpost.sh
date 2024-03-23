#!/bin/bash
# Script Get,Put,Del,Post - Code By Sachi Henakyy.

http_get() {
    local url="$1"
    local headers="$2"
    local output_file="$3"
    curl -L -X GET -H "$headers" "$url" -o "$output_file"
}

http_put() {
    local url="$1"
    local data="$2"
    local headers="$3"
    local output_file="$4"
    curl -L -X PUT -d "$data" -H "$headers" "$url" -o "$output_file"
}

http_del() {
    local url="$1"
    local headers="$2"
    local output_file="$3"
    curl -L -X DELETE -H "$headers" "$url" -o "$output_file"
}

http_post() {
    local url="$1"
    local data="$2"
    local headers="$3"
    local output_file="$4"
    curl -L -X POST -d "$data" -H "$headers" "$url" -o "$output_file"
}

echo "Masukan URL: "
read url
echo "Masukan headers.txt: "
read headers_file
echo "Pilih Method-Nya (GET, PUT, DEL, POST): "
read method

if [ "$method" != "GET" ] && [ "$method" != "PUT" ] && [ "$method" != "DEL" ] && [ "$method" != "POST" ]; then
    echo "Metode Permintaan Tidak Valid. Keluar."
    exit 1
fi

echo "Masukkan Data (jika ada): "
read data
echo "Masukkan Jalur Untuk Menyimpan File Output: "
read output_file

headers=$(cat "$headers_file")

case "$method" in
    "GET")
        http_get "$url" "$headers" "$output_file"
        ;;
    "PUT")
        http_put "$url" "$data" "$headers" "$output_file"
        ;;
    "DEL")
        http_del "$url" "$headers" "$output_file"
        ;;
    "POST")
        http_post "$url" "$data" "$headers" "$output_file"
        ;;
esac

echo "Tanggapan Disimpan KeFile: $output_file"
