module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['@testing-library/jest-dom'],
  moduleNameMapper: {
    '\\.(css)$': '<rootDir>/src/__mocks__/styleMock.js',
  },
}
