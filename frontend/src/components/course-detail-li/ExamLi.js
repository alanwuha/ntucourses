import React from 'react';

function renderExamDates(exams) {
    let result = exams.map(exam => {
        return exam.date + ' ' + exam.day + ' ' + exam.time + ' ' + exam.duration + 'HRS (' + getSemesterDisplay(exam.semester) + ')'
    })
    return result.join(' || ');
}

function getSemesterDisplay(sem) {
    if (sem <= 3) {
        return 'Sem ' + sem
    } else if(sem === 4) {
        return 'Special Term 1'
    } else if(sem === 5) {
        return 'Special Term 2'
    } else {
        return ''
    }
}

function ExamLi(props) {
    let result = null;
    if(Array.isArray(props.exams) && props.exams.length) {
        result = (
            <li data-toggle="tooltip" title="Exam">
                <span style={{fontWeight: 100}} className="li-span">Exam</span>
                &nbsp;
                {renderExamDates(props.exams)}
            </li>
        )
    }

    return result;
}

export default ExamLi;