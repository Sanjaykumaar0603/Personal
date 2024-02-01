import { spawn } from 'child_process';
import fs from 'fs';

const pythonProcess = spawn('python', ['C:\\Users\\sanja\\Documents\\Coding\\SpaceHCK\\space.py']);

let userInputDataset = [];
let recommendedActions = [];

pythonProcess.stdout.on('data', (data) => {
  const outputString = data.toString();

  // Assuming the output format is like "User Input Dataset: [...]\nRecommended Actions: [...]"
  const userInputMatch = outputString.match(/User Input Dataset: \[(.*?)\]/);
  const recommendedActionsMatch = outputString.match(/Recommended Actions: \[(.*?)\]/);

  if (userInputMatch) {
    userInputDataset = userInputMatch[1].split(', ').map(item => item.trim());
  }

  if (recommendedActionsMatch) {
    recommendedActions = recommendedActionsMatch[1].split(', ').map(item => item.trim());
  }
});

pythonProcess.on('close', (code) => {
  console.log('User Input Dataset:', userInputDataset);
  console.log('Recommended Actions:', recommendedActions);
  console.log(`Python script exited with code ${code}`);

  // Write recommendedActions to CSV file
  const csvData = recommendedActions.map(item => item.split(',').map(subItem => subItem.trim()).join(',')).join(',');

  fs.writeFile('C:\\Users\\sanja\\Documents\\Coding\\SpaceHCK\\recommendedActions.csv', csvData, (err) => {
    if (err) {
      console.error('Error writing to CSV file:', err);
    } else {
      console.log('Recommended Actions written to recommendedActions.csv');
    }
  });
});

// Add any necessary error handling
pythonProcess.on('error', (err) => {
  console.error(`Error executing Python script: ${err}`);
});
