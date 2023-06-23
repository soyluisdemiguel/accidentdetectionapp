import React, { useState } from 'react';

function UserFeedback() {
  const [feedback, setFeedback] = useState('');

  const handleFeedbackChange = (e) => {
    setFeedback(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert('Thank you for your feedback!');
    setFeedback('');
  };

  return (
    <div className="user-feedback">
      <h2>User Feedback</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          value={feedback}
          onChange={handleFeedbackChange}
          placeholder="Share your feedback or report an accident"
          rows="5"
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default UserFeedback;
