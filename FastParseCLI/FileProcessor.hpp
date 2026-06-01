#ifndef FILE_PROCESSOR_HPP
#define FILE_PROCESSOR_HPP

#include <string>
#include <string_view>
#include <vector>
#include <filesystem>
#include <future>
#include <mutex>

class FileProcessor {
public:
    explicit FileProcessor(std::string_view targetToken);
    ~FileProcessor() = default;

    void scanDirectory(const std::filesystem::path& directoryPath);
    void printResults() const;

private:
    void processFile(const std::filesystem::path& filePath);

    std::string token;
    std::vector<std::future<void>> futures;
    mutable std::mutex mutex;

    uint64_t totalFilesProcessed{ 0 };
    uint64_t totalMatchesFound{ 0 };
};

#endif