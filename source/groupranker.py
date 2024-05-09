import re
import sys
import datetime

def main():
  chatPath = sys.argv[1]
  chatStream = open(chatPath, 'r')
  chatContent = chatStream.read()

  messageMatches = re.findall(r'\[(\d{2})/(\d{2})/(\d{4}), \d{1,2}:\d{2}:\d{2} [AP]M\] (?:~ )?([^:]+):', chatContent)

  firstDay, firstMonth, firstYear, firstAuthor = messageMatches[0]
  firstTime = datetime.datetime.strptime(f'{firstDay}/{firstMonth}/{firstYear}', r'%d/%m/%Y')
  
  lastDay, lastMonth, lastYear, lastAuthor = messageMatches[-1]
  lastTime = datetime.datetime.strptime(f'{lastDay}/{lastMonth}/{lastYear}', r'%d/%m/%Y')

  existingTimes = [firstTime]

  while existingTimes[-1] < lastTime:
    currentTime = existingTimes[-1] + datetime.timedelta(days=7)
    existingTimes.append(currentTime)
  
  existingAuthors = {}
  
  for messageMatch in messageMatches:
    currentDay, currentMonth, currentYear, currentAuthor = messageMatch
    currentTime = datetime.datetime.strptime(f'{currentDay}/{currentMonth}/{currentYear}', r'%d/%m/%Y')

    if not currentAuthor in existingAuthors:
      existingAuthors[currentAuthor] = {}

      for existingTime in existingTimes:
        existingAuthors[currentAuthor][existingTime] = 0
  
    for existingTime in existingAuthors[currentAuthor]:
      if currentTime <= existingTime:
        existingAuthors[currentAuthor][existingTime] += 1
    
  outputCsv = 'name'
  outputPath = re.sub(r'\.[^.]*$', '.csv', chatPath)
  outputFile = open(outputPath, 'w')

  for existingTime in existingTimes:
    existingDate = existingTime.strftime(r'%d/%m/%Y')
    outputCsv += f',{existingDate}'
  
  for existingAuthor in existingAuthors:
    outputCsv += f'\n{existingAuthor}'
    for existingTime in existingAuthors[existingAuthor]:
      outputCsv += f',{existingAuthors[existingAuthor][existingTime]}'
  
  outputFile.write(outputCsv)

if __name__ == '__main__':
  main()