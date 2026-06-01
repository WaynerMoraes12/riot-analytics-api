#include "FileProcessor.hpp"
#include <fstream>
#include <iostream>

FileProcessor::FileProcessor(std::string_view targetToken)
    : token(targetToken) {
}

void FileProcessor::scanDirectory(const std::filesystem::path& directoryPath) {
    if (!std::filesystem::exists(directoryPath) || !std::filesystem::is_directory(directoryPath)) {
        std::cerr << "Erro: Diretorio invalido ou inexistente.\n";
        return;
    }

    for (const auto& entry : std::filesystem::recursive_directory_iterator(directoryPath, std::filesystem::directory_options::skip_permission_denied)) {
        if (entry.is_regular_file()) {
            futures.push_back(std::async(std::launch::async, &FileProcessor::processFile, this, entry.path()));
        }
    }

    for (auto& future : futures) {
        future.wait();
    }
}

void FileProcessor::processFile(const std::filesystem::path& filePath) {
    std::ifstream file(filePath, std::ios::binary);
    if (!file.is_open()) return;

    std::string line;
    uint64_t localMatches = 0;

    while (std::getline(file, line)) {
        size_t pos = 0;
        while ((pos = line.find(token, pos)) != std::string::npos) {
            ++localMatches;
            pos += token.length();
        }
    }

    std::lock_guard<std::mutex> lock(mutex);
    totalMatchesFound += localMatches;
    ++totalFilesProcessed;
}

void FileProcessor::printResults() const {
    std::lock_guard<std::mutex> lock(mutex);
    std::cout << "--------------------------------------\n";
    std::cout << "Arquivos processados: " << totalFilesProcessed << "\n";
    std::cout << "Ocorrencias encontradas: " << totalMatchesFound << "\n";
    std::cout << "--------------------------------------\n";
}