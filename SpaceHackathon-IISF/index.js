// Import necessary modules
import express from "express";
import axios from "axios";
import { stringify } from "csv-stringify";
import { dirname } from "path";
import { fileURLToPath } from "url";
import fs from "fs";
import path from "path";
import { format } from 'date-fns';
import { promises as fsPromises } from 'fs';
//import { runPythonScript } from './public/rec'; // Adjust the path accordingly
//import getDivNames from './public/rec'; // Adjust the path accordingly




// Set up directory name for __dirname in ES6 environment
const __dirname = dirname(fileURLToPath(import.meta.url));

// Initialize express app
const app = express();
const port = 6969;

// Middleware setup
app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));
app.use(express.text());
app.use(express.static(path.join(__dirname, 'public')));

// Set the view engine to ejs
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', (req, res) => {
  runPythonScript((result) => {
    if (result.error) {
      console.error(result.error);
      res.status(500).send('Internal Server Error');
    } else {
      res.render('index', {
        userInputDataset: result.userInputDataset,
        recommendedActions: result.recommendedActions,
        exitCode: result.exitCode,
        getDivNames,
      });
    }
  });
});

// Update CSV file route
app.post('/updateCsv', (req, res) => {
  const csvData = req.body;
  const filePath = path.join(__dirname, 'log_events.csv');

  fs.readFile(filePath, 'utf8', (err, existingData) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Internal Server Error');
    }

    const newData = existingData + csvData;

    fs.writeFile(filePath, newData, (err) => {
      if (err) {
        console.error(err);
        return res.status(500).send('Internal Server Error');
      }

      res.status(200).send('CSV Updated Successfully');
    });
  });
});

// Function to create a filtered copy of the CSV
function createFilteredCopy(originalFilePath, newCopyFilePath, userLogsFolder) {
  fs.readFile(originalFilePath, 'utf8', async (err, data) => {
    if (err) {
      console.error('Error reading file:', err);
      return;
    }

    if (!data.trim()) {
      console.log('Input file is empty, no changes made.');
      return;
    }

    const lines = data.split('\n');
    const extractedData = lines.map(line => {
      const parts = line.split(',');
      if (parts[0] === 'Hover' || parts[0] === 'Link Click') {
        return parts[1];
      }
    }).filter(Boolean);

    const currentDate = format(new Date(), 'yyyy-MM-dd HH:mm:ss');
    const newLine = `'${currentDate}',${extractedData.join(',')}`;

    fs.appendFile(newCopyFilePath, newLine + '\n', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
        return;
      }
      console.log('File updated successfully.');
    });

    const formattedDateForFilename = format(new Date(), 'yyyy-MM-dd_HH-mm-ss');
    const userLogsFileName = `${formattedDateForFilename}.csv`;
    const userLogsFilePath = path.join(userLogsFolder, userLogsFileName);

    try {
      await fsPromises.copyFile(originalFilePath, userLogsFilePath);
      console.log(`File copied to userlogs as ${userLogsFileName} successfully.`);
      await fsPromises.writeFile(originalFilePath, '');
      console.log('Original file contents cleared.');
    } catch (copyErr) {
      console.error('Error during file copy or clear:', copyErr);
    }
  });
}

// Route to handle user closing the website
app.post('/user-closed', (req, res) => {
  const originalFilePath = 'log_events.csv';
  const newCopyFilePath = 'C:\\Users\\sanja\\Documents\\Coding\\SpaceHCK\\data csv\\data.csv';
  const userLogsFolder = 'C:\\Users\\sanja\\Documents\\Coding\\SpaceHCK\\userlogs';

  createFilteredCopy(originalFilePath, newCopyFilePath, userLogsFolder);

  res.status(200).send('Process initiated');
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
