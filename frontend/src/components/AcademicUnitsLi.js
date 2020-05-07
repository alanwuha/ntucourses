import React from 'react';

function AcademicUnitsLi(props) {
    let result = null;
    
    if(props.academic_units) {
        result = (
            <li data-toggle="tooltip" title="Academic Units">
                {/* <span aria-hidden="true" className="fa fa-book icon-fact"></span> */}
                <span style={{fontWeight: '100'}} className="badge badge-light">Academic units</span>
                &nbsp;
                {props.academic_units.toFixed(1)}
            </li>
        )
    }

    return result;
}

export default AcademicUnitsLi;